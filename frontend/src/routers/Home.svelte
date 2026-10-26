<script>
    import Router from 'svelte-spa-router'
    import Home from "./routes/Home.svlete"

    const routes = {
        '/' : Home,
    }
</script>

<Router {routes}></Router>