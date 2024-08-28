
function handle_form_fetch(event, request_form) {
    trip_id = (event.target.dataset.targettripid)
    if (!event.target.matches('.collapsed')){
        fetch_bookingreq_forms(trip_id, request_form)
    }
}

async function fetch_bookingreq_forms(trip_id, request_form) {
    
    let response;

    if (request_form){
        response = await fetch(`/give_bookingreq_forms/${trip_id}`);
    } else {
        response = await fetch(`/give_bookingreqs_list/${trip_id}`);
    }
    if (response.ok) {
        const data = await response.json();
        const bookingFormsHtml = data.rendered_form;
        const targetDiv = document.getElementById(`form_space_${trip_id}`);
        targetDiv.innerHTML = bookingFormsHtml;
    } else {
        console.error('Failed to fetch details', response.statusText);
    }
}