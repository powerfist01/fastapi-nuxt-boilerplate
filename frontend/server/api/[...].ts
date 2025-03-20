import { joinURL } from 'ufo'

export default defineEventHandler(async (event) => {
    // Get the runtimeconfig proxy url
    
    const proxyUrl = useRuntimeConfig().public.proxyUrl;
    // check the path
    const target = joinURL(proxyUrl, event.path)

    // proxy it!
    return proxyRequest(event, target)
})
