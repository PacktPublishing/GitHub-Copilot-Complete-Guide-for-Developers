document.addEventListener('DOMContentLoaded', () => {
    console.log("Add drag-and-drop functionality here.");
    // Future implementation for drag-and-drop

    const headers = document.querySelectorAll('.column h2');
    headers.forEach(header => {
        if (header.textContent.trim() === "Doing") {
            header.style.backgroundColor = "#4CAF50"; // Green
            header.style.color = "white";
        } else if (header.textContent.trim() === "Done") {
            header.style.backgroundColor = "#2196F3"; // Blue
            header.style.color = "white";
        }
    });
});
