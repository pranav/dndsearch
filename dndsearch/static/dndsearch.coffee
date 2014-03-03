# DndSearch

# Get the JSON back from the search
@search = (terms) ->
    data = ''
    $.ajax({
        url: '/query/' + terms,
        dataType: 'json',
        method: 'GET',
        async: false,
        success: (e) ->
            data = e
    })
    return data


@build_table = (results) ->
    table = '
        <table class="table table-striped table-hover">
            <thead><tr><td>Book</td><td>Page</td></tr></thead>
            <tbody>'

    for o in results
        console.log o
        table += '<tr><td>'+o.book+'</td><td>'+o.page+'</td></tr>'

    table += '</tbody></table>'
    return table
    


$(document).ready () ->
    $('form').submit (e) ->
        e.preventDefault()
        search_term = $('input').val()

        $('#results').html(build_table(search(search_term)))
