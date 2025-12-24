#!/bin/bash
set -ueo pipefail


echoerr() {
    >&2 echo "$@"
}


fail() {
    echoerr Failure "$1" - "$2"
    echo -en "HTTP/1.1 $1 $2\r\n\r\n$3\r\n"
    exit
}


handle_root() {
    echo -en 'HTTP/1.1 200\r\nContent-Type: text/html\r\n\r\n'
    cat << EOF
<!DOCTYPE html>
<style>
html, body, .container {
    height: 100%;
}

.container {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>

<html><body><div class="container">
Everything is possible at zombo.com!
</div></body></html>
EOF
}


handle_favicon() {
    read b64 << EOF
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAMFBMVEU0OkArMjhobHEoPUPFEBIu\
O0L+AAC2FBZ2JyuNICOfGx7xAwTjCAlCNTvVDA1aLzQ3COjMAAAAVUlEQVQI12NgwAaCDSA0888G\
CItjn0szWGBJTVoGSCjWs8TleQCQYV95evdxkFT8Kpe0PLDi5WfKd4LUsN5zS1sKFolt8bwAZrCa\
GqNYJAgFDEpQAAAzmxafI4vZWwAAAABJRU5ErkJggg==
EOF
    pnglen=$(echo $b64 | base64 --decode | wc -c)
    echo -en 'HTTP/1.1 200\r\n'
    echo -en 'Content-Type: image/png\r\n'
    echo -en 'Content-Length: '${pnglen}'\r\n'
    echo -en '\r\n'
    echo $b64 | base64 --decode
}


handle_request() {
    echoerr 'Connection accepted'
    read -t 1 method url whatever
    let cnt=0
    echoerr $cnt: $method $url $whatever
    while read -t 1 line; do
        let cnt++
        echoerr $cnt: $line
        [[ $line =~ ^[[:space:]]*$ ]] && break
    done

    [[ $method != GET ]] && fail 405 "MethodNotAllowed" "Method Not Allowed"

    case "$url" in
        "/") handle_root ;;
        "/favicon.ico") handle_favicon ;;
        *) fail 404 NotFound "Page not found" ;;
    esac
    echoerr Success 200
}


export -f echoerr fail handle_root handle_favicon handle_request


my_location=$(readlink -f "$0")
my_mod_time=$(stat -c %Y "$my_location")
while [ : ]; do
    new_mod_time=$(stat -c %Y "$my_location")
    if [[ $my_mod_time != $new_mod_time ]]; then
        # hot reloading! Requires F5 in the browser.
        exec "$my_location" "$@"
    fi
    # -k allows multiple simultaneous connections but disables hot reloading
    keepalive=
    # keepalive=-k
    ncat -lvp 8080 $keepalive -c "/bin/bash -c handle_request"
done
