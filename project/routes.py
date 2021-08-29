from project.views import Index, About, Other

routes = {
    '/': Index(),
    '/about/': About(),
    '/other/': Other()
}