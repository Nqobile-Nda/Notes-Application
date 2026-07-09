document.addEventListener("DOMContentLoaded", async() => {

    const notificationBar = document.getElementById("notification-bar");
    const myForm = document.getElementById("myForm");
    const notesArea = document.getElementById("notesArea");


    async function loadNotes() {
        const response = await fetch("/load_notes")
        const notes = await response.json()
        return notes
    }


    async function renderNotes() {
        const notes = await loadNotes()
        notesArea.innerHTML = notes.map(note => {
            `<p>${note.title}</p>
            <p>${note.content}</p>`
        })
    }


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
        } 
        
        catch (error) {
            notificationBar.textContent = "Network error. Please try again.";
        }
    }  

    myForm.addEventListener("submit", (e) => {
        e.preventDefault();
        addNote();
        myForm.reset();
    })
});