document.addEventListener('DOMContentLoaded', ()=>{

    updateActiveStatus()

    unread_messagecount_space = document.getElementById('unread_messagecount_space')

    if (unread_messagecount_space) {
        update_unread_looks()
    }
})

async function update_unread_looks() {

    const unread_count = await get_unread_counter()
    unread_messagecount_space.innerText = unread_count

    if (unread_count){
        unread_messagecount_space.classList.remove('visually-hidden')
    } else {
        unread_messagecount_space.classList.add('visually-hidden')
    }

}

async function get_unread_counter() {

    const response = await fetch('/give_unread')
    const data = await response.json()
    unread_count = data.unread
    if (unread_count){
        return unread_count
    } else {
        return 0
    }
}

function fetchActiveRoute() {

    let activeroute = location.pathname
    return (activeroute)
    
}

function updateActiveStatus() {
    
    let links = top_bar.querySelectorAll(".nav-link")
    let activeRoute = fetchActiveRoute()
    
    links.forEach((link)=>{
        
        if (link.pathname==activeRoute) {
            link.classList.add("active")
            link.ariaCurrent = "page"
        } else {
            link.classList.remove("active")
            link.removeAttribute("ariaCurrent")
        }

    })

    document.addEventListener('scroll', ()=>{

        if (window.scrollY === 0) {
            top_bar.classList.add("at_top");
            top_bar.classList.remove("not_at_top");
        } else {
            top_bar.classList.add("not_at_top");
            top_bar.classList.remove("at_top");
        }

    })


}