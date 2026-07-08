document.addEventListener("DOMContentLoaded", async() => {

    const notificationBar = document.getElementById("notification-bar");
    const myForm = document.getElementById("myForm");

    async function addNote() {
        const data = {
            title: myForm.note_title.value,
            content: myForm.note_content.value
        };

        try {
            const response = await fetch("/api/form", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            if (!response.ok) {
                notificationBar.textContent = result.error || "Failed to submit note.";
            } else {
                notificationBar.textContent = result.success;
            }
        } catch (error) {
            notificationBar.textContent = "Network error. Please try again.";
        }
    }  

    myForm.addEventListener("submit", (e) => {
        e.preventDefault();
        addNote();
        myForm.reset();
    })
});