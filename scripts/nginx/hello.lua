server {
    listen       8082;
    server_name  localhost;

    #charset koi8-r;

    access_log  /var/log/nginx/ahcming-access.log  main;
    location /hi {
        default_type text/html;
        content_by_lua '
            local remoteIp = ngx.var.remote_addr or "0.0.0.0"
            local currTime = os.date("%Y-%m-%d %H:%M:%S");

            ngx.say("<p>hello, " .. remoteIp .. "</p>")
            ngx.say("<p>welcome to nginx lua world!</p>")
            ngx.say("<p>@" .. currTime .. "</p>");
        ';
    }       
}    
