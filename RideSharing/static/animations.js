document.addEventListener('DOMContentLoaded', function() {

    const post_form_collapse = document.getElementById('post_form_collapse')
    const post_form_collapse_span = document.getElementById('post_form_collapse_span')

    post_form_collapse.addEventListener('click', ()=>{
        
        post_form_collapse.classList.toggle('btn-primary')
        post_form_collapse_span.style.width = post_form_collapse_span.style.width==='100%'?'0%':'100%'
        post_form_collapse_span.classList.toggle('animation_div_size')
       
    })

    post_form_collapse_span.addEventListener('animationend', ()=>{
        post_form_collapse_span.classList.toggle('animation_div_size')
        post_form_collapse_span.style.animationDirection = post_form_collapse_span.style.animationDirection==='normal'?'reverse':'normal'

    })

});