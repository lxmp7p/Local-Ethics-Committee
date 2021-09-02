$(document).ready(function() {
    $("#input-43").fileinput({
        showPreview: false,
        allowedFileExtensions: ["docx", "word", "pdf", "txt"],
        elErrorContainer: "#errorBlock",
        showRemove: false,
        showUpload: false,
    });
});