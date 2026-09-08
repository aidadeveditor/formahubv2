/* Formahub — stockage de la sauvegarde chiffrée (Cloudflare Pages Function)
 *
 * L'identifiant reçu est un condensé SHA-256 du code secret, calculé dans
 * le navigateur : le code lui-même n'arrive jamais ici. Le corps est un
 * bloc AES-GCM que ce Worker se contente de ranger et de rendre.
 *
 * GET    /api/progress/<id>  → le dernier bloc enregistré, ou {}
 * POST   /api/progress/<id>  → remplace le bloc
 * DELETE /api/progress/<id>  → efface la sauvegarde
 */

const ID_RE = /^[a-f0-9]{8,64}$/;
const MAX_BYTES = 512 * 1024;      // largement au-dessus d'une progression complète

const JSON_HEADERS = {
  'Content-Type': 'application/json; charset=utf-8',
  'Cache-Control': 'no-store',
  'X-Content-Type-Options': 'nosniff'
};

function json(body, status = 200) {
  return new Response(typeof body === 'string' ? body : JSON.stringify(body), {
    status,
    headers: JSON_HEADERS
  });
}

function validId(id) {
  return typeof id === 'string' && ID_RE.test(id);
}

export async function onRequestGet(context) {
  const { params, env } = context;
  if (!validId(params.id)) return json({ error: 'identifiant invalide' }, 400);
  if (!env.PROGRESS_KV) return json('{}');
  const data = await env.PROGRESS_KV.get(`progress:${params.id}`);
  return json(data || '{}');
}

export async function onRequestPost(context) {
  const { params, env, request } = context;
  if (!validId(params.id)) return json({ error: 'identifiant invalide' }, 400);

  const body = await request.text();
  if (body.length > MAX_BYTES) return json({ error: 'sauvegarde trop volumineuse' }, 413);
  try {
    JSON.parse(body);
  } catch (e) {
    return json({ error: 'corps illisible' }, 400);
  }

  if (!env.PROGRESS_KV) return json({ ok: true, local: true });
  await env.PROGRESS_KV.put(`progress:${params.id}`, body);
  return json({ ok: true, bytes: body.length });
}

export async function onRequestDelete(context) {
  const { params, env } = context;
  if (!validId(params.id)) return json({ error: 'identifiant invalide' }, 400);
  if (!env.PROGRESS_KV) return json({ ok: true, local: true });
  await env.PROGRESS_KV.delete(`progress:${params.id}`);
  return json({ ok: true });
}
