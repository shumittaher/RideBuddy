function handle_bookingReqConf(event) {

    const req_id = event.currentTarget.dataset.itemId
    const save_action = event.currentTarget.dataset.saveAction == "True"
    const trip_id = event.currentTarget.dataset.tripId

    send_bookingStatUpdate(req_id, save_action, trip_id)

}

async function send_bookingStatUpdate(req_id, save_action, trip_id) {            //save_action will be true for save and false for delete 

    const response = await fetch(
        '/booking_request',
        {
            method: 'PUT',
            headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
            },
            body: JSON.stringify({
                'req_id' : req_id,
                'save_action' : save_action
            })
        }
    )

    const data = await response.json()
    
    if (response.ok) {
        const open_spots = (data.open_spots)
        
        update_row_look(`requestrow-${req_id}`, data.message, data.status)
        update_open_spots(open_spots, trip_id)
    }
    
}

function update_open_spots(open_spots, trip_id) {

    const open_spots_space = document.getElementById(`open_spots_${trip_id}`)
    open_spots_space.textContent = open_spots        
}

function update_row_look(row_id, message, status) {

    const requestrow = document.getElementById(row_id)
    const tds = requestrow.querySelectorAll('td');

    switch (status) {

        case 'saved':
            var row_color = 'text-bg-success'
            var disable_status = false
            break;
    
        case 'deleted':
            var row_color = 'text-bg-danger'
            var disable_status = true
            break;

        case 'warning':
            var row_color = 'text-bg-warning'
            var disable_status = false
            break;
    }

    tds.forEach(td => {
        td.classList.add(row_color);

        if (td.classList.contains('status')) {
            td.textContent = message;
        }
            
        const buttons = td.querySelectorAll('button');
        buttons.forEach(button => {
            button.disabled = disable_status;
        });

    });

}

function handle_showBookingReq(event) {

    itemId = event.currentTarget.dataset.reqId

    const infoModal = document.getElementById(`infoModal-${itemId}`)
    
    const modal = new bootstrap.Modal(infoModal)

    modal.show()

}
