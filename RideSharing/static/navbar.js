document.addEventListener('DOMContentLoaded', ()=>{

    updateActiveStatus()

    if (location.pathname=='/') {
        top_bar.classList.add("navbar-dark")
    }

    unread_messagecount_space = document.getElementsByClassName('unread_messagecount_space')

    if (unread_messagecount_space) {
        update_unread_looks()
    }
})

async function update_unread_looks() {

    const unread_count = await get_unread_counter()

    spaces = [...unread_messagecount_space]
    spaces.forEach((space)=>{

        console.log(space)
        space.innerText = unread_count
        
        if (unread_count){
            space.classList.remove('visually-hidden')
        } else {
            space.classList.add('visually-hidden')
        }
        
    }
    )
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

function updateActiveStatus() {
    
    let links = top_bar.querySelectorAll(".nav-link")
    let activeRoute = location.pathname
    
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
            top_bar.classList.add("at_top", activeRoute=='/'?"navbar-dark":"_");
            top_bar.classList.remove("not_at_top"); 
        } else {
            top_bar.classList.add("not_at_top");
            top_bar.classList.remove("at_top", activeRoute=='/'?"navbar-dark":"_");
        }
            
    })


}