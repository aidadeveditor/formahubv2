export async function onRequestGet(context) {
  const { params, env } = context;
  if (!env.PROGRESS_KV) return new Response('{}', { headers: { 'Content-Type': 'application/json' } });
  const data = await env.PROGRESS_KV.get(`progress:${params.id}`);
  return new Response(data || '{}', {
    headers: { 'Content-Type': 'application/json' }
  });
}

export async function onRequestPost(context) {
  const { params, env, request } = context;
  if (!env.PROGRESS_KV) return new Response(JSON.stringify({ ok: true, local: true }), { headers: { 'Content-Type': 'application/json' } });
  const body = await request.text();
  await env.PROGRESS_KV.put(`progress:${params.id}`, body);
  return new Response(JSON.stringify({ ok: true }), {
    headers: { 'Content-Type': 'application/json' }
  });
}