function fetchActiveRoute() {

    let activeroute = location.pathname

    console.log(activeroute)
    return (activeroute)
    
}

function updateActiveStatus() {
    
    let links = document.querySelectorAll(".nav-link")
    let activeRoute = fetchActiveRoute()
    
    for (let index = 0; index < links.length-1; index++) {
        
        console.log(links[index].pathname)

        if (links[index].pathname==activeRoute) {
            links[index].classList.add("active")
            links[index].ariaCurrent = "page"
            break
        } else {
            links[index].classList.remove("active")
            links[index].removeAttribute("ariaCurrent")
        }
                
        }
}

updateActiveStatus()