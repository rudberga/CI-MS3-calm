// Function to render the artist in the DOM after it is inserted in the DataBase
function renderArtist(artist) {
    // If vocals is ON print microphone icon, if it is OFF print microphone with slash icon
    let vocalsIcon;
    if (artist.vocals == "on") {
        vocalsIcon = '<i class="fas fa-microphone"></i>';
    } else {
        vocalsIcon = '<i class="fas fa-microphone-slash"></i>';
    }
    // Prepend the artist element to the container
    $("#artists_container").prepend(`
        <div class="col s12 m4">
            <div class="card small">
                <div class="card-image waves-effect waves-block waves-light">
                    <img class="activator" src="${artist.image}">
                </div>
                <div class="card-content">
                    <span class="card-title activator grey-text text-darken-4"><strong>${artist.artist_name}</strong>
                        <a href="${artist.spotify}" target="_blank"><i class="fab fa-spotify"></i></a>
                        <p>${artist.genre_name}</p>
                </div>
                <div class="card-reveal">
                    <span class="card-title grey-text text-darken-4"><strong>${artist.artist_name} </strong><i
                            class="fas fa-chevron-down right"></i></span>
                    <p>Genre: ${artist.genre_name}</p>
                    <p>Nationality: ${artist.nationality}</p>
                    Vocals: ${vocalsIcon}
                    <p><em>Added by: ${artist.created_by}</em></p>
                    <a href="/delete_artist/${artist._id}"
                        onclick="return confirm('Do you want to delete this artist?');"
                        class="btn-delete right"><i class="fas fa-trash-alt"></i></a>
                    <a href="/edit_artist/${artist._id}"
                        class="btn-edit right"><i class="fas fa-edit"></i></a>
                </div>
            </div>
        </div>
    `);
}
//Function to run when a new artist is added
$("#add_artist_form").on("submit", function(e) {
    // Prevent default behavior on submit
    e.preventDefault();
    // Construct the data object to be sent to the server
    let artist = {
        // Store each of the form values
        genre_name: $("#genre_name").val(),
        artist_name: $("#artist_name").val(),
        nationality: $("#nationality").val(),
        image: $("#image").val(),
        spotify: $("#spotify").val(),
    }
    // If "vocals" is checked, add the vocals item to the data to be sent to the server
    if ($("#vocals").prop("checked")) {
        artist.vocals = "on";
    }
    // Make the AJAX Request
    $.ajax({
        // Set the url of the request to be the same as the form's URL
        url: $("#add_artist_form").attr("action"),
        // Make the request as POST
        type: "POST",
        // Set the data to be sent to the server
        data: artist,
        // Function to run when request is successful
        success: function (response) {
            // Artist is returned as a String, so we parse it to convert it to a JSON object
            let json = JSON.parse(response);
            // Id of the artist is returned as an object, so store the content of the object in the key "_id"
            json._id = json._id.$oid;
            // Close the modal
            $("#modal3").modal("close");
            // If "No Results found" text, remove it (text displayed when there are no artists shown)
            if ($("#no_results_text")) {
                $("#no_results_text").remove();
            }
            // Clear the modal inputs
            $("#artist_name").val("");
            $("#nationality").val("");
            $("#image").val("");
            $("#spotify").val("");
            $("#vocals").prop("checked", false);
            // Display the artist inserted
            renderArtist(json);
        },
        // Function to run when request throws error
        error: function (xhr, ajaxOptions, thrownError) {
        if (xhr.status == 200) {
            console.log(ajaxOptions);
        } else {
            console.log(xhr.status);
            console.log(thrownError);
        }
        },
    });
});