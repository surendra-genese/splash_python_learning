-- simple basic example of lua script
function main(splash)
    splash:go('www.surenguide.com')

    splash:wait(0.15)
    return "open the site"
end
