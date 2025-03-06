document.addEventListener("DOMContentLoaded", function () {
    var socket = io.connect("http://" + window.location.hostname + ":" + location.port);
    var doc_id = document.getElementById("content").dataset.docId;
    var titleInput = document.getElementById("title");
    var contentArea = document.getElementById("content");

    socket.emit("join_document", { doc_id: doc_id });

    function sendUpdate() {
        socket.emit("edit_document", { 
            doc_id: doc_id, 
            title: titleInput.value, 
            content: contentArea.value 
        });
    }

    titleInput.addEventListener("input", sendUpdate);
    contentArea.addEventListener("input", sendUpdate);

    socket.on("update_document", function (data) {
        titleInput.value = data.title;  
        contentArea.value = data.content;
    });
});
