document.addEventListener('DOMContentLoaded', function () {
    // Function to toggle the display of the edit form
    function toggleEditForm(entryId) {
        const entryContentElement = document.querySelector(`#entry-content-${entryId}`);
        const editFormElement = document.querySelector(`#edit-form-${entryId}`);

        // Check if elements exist before modifying their style
        if (entryContentElement && editFormElement) {
            // Toggle the visibility of post content and edit form
            if (entryContentElement.style.display === 'none') {
                entryContentElement.style.display = 'block';
                editFormElement.style.display = 'none';
            } else {
                entryContentElement.style.display = 'none';
                editFormElement.style.display = 'block';
            }
        }
    }

    // Show Favorited Entries Button Functionality
    const showFavourizedButton = document.querySelector('#show-favourized-button');
    showFavourizedButton.onclick = function () {
        // Toggle the visibility of favorited entries
        const favourizedEntries = document.querySelectorAll('.favourized');
        favourizedEntries.forEach(function (entry) {
            if (entry.style.display === 'none' || entry.style.display === '') {
                entry.style.display = 'block';
            } else {
                entry.style.display = 'none';
            }
        });
    };

// Comment Button Functionality
document.querySelectorAll('.comment-button').forEach(function (button) {
    button.onclick = function () {
        const entryId = button.dataset.entryId;
        const commentModal = document.querySelector(`#comment-modal-${entryId}`);

        if (commentModal.style.display === 'none' || commentModal.style.display === '') {
            commentModal.style.display = 'block';
        } else {
            commentModal.style.display = 'none';
        }
    };
});

// Save Comment Button Functionality
document.querySelectorAll('.save-comment-button').forEach(function (button) {
    button.onclick = function () {
        const entryId = button.dataset.entryId;
        const commentContent = document.querySelector(`#comment-modal-${entryId} textarea[name="comment_content"]`).value;

        // Debugging: Log the comment content before sending the request
        console.log('Comment content:', commentContent);

        // Send the comment content via AJAX to add the comment
        fetch(`/add_comment/${entryId}/`, {
            method: 'POST',
            body: JSON.stringify({ comment_content: commentContent }),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,  // Include the CSRF token
            },
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {

                // Close the comment modal
                const commentModal = document.querySelector(`#comment-modal-${entryId}`);
                commentModal.style.display = 'none';

                // Add the new comment to the comment section, if you have one
                const commentSection = document.querySelector(`#comment-section-${entryId}`);
                const newComment = document.createElement('div');
                newComment.className = 'comment';
                newComment.textContent = commentContent;
                commentSection.appendChild(newComment);

            } else {
                alert('Error adding a comment: ' + data.error_message);
            }
        })
        .catch((error) => {
            alert('Error adding a comment.');
            console.error(error);
        });
    };
});

// Favourize Button Functionality
document.querySelectorAll('.btn-favourize').forEach(function (button) {
    button.onclick = function () {
        const entryId = button.dataset.entryId;

        fetch(`/favourize_entry/${entryId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
            },
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                // Update the like status and count
                const favourizeButton = document.querySelector(`#favourize-button-${entryId}`);

                if (data.favourized) {
                    favourizeButton.textContent = 'Unfavourize'; // Updated text
                } else {
                    favourizeButton.textContent = 'Favourize'; // Updated text
                }
            } else {
                alert('Error favourizing entry: ' + data.error_message);
            }
        })
        .catch((error) => {
            alert('Error favourizing entry.');
            console.error(error);
        });
    };
});

// Edit Button Functionality
document.querySelectorAll('.edit-button').forEach(function (button) {
    button.onclick = function () {
        const entryId = button.dataset.entryId;
        toggleEditForm(entryId);
    };
});

    // Save Edit Button Functionality
    document.querySelectorAll('.save-button').forEach(function (button) {
        button.onclick = function () {
            const entryId = button.dataset.entryId;

            // Get the edited content from the textarea
            const editedContent = document.querySelector(`#edit-content-${entryId}`).value;

            // Debugging: Log the edited content before sending the request
            console.log('Edited content:', editedContent);

            // Send the edited content via AJAX to update the post
            fetch(`/edit_entry/${entryId}/`, {
                method: 'POST',
                body: JSON.stringify({ content: editedContent }),
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,  // Include the CSRF token
                },
            })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    // Update the entry content with the edited content
                    document.querySelector(`#entry-content-${entryId}`).textContent = data.content;
                    toggleEditForm(entryId); // Hide the edit form

                } else {
                    alert('Error updating entry: ' + data.error_message);
                }
            })
            .catch((error) => {
                alert('Error updating entry.');
                console.error(error);
            });
        };
    });
});

// Delete Button Functionality
document.querySelectorAll('.delete-button').forEach(function (button) {
    button.onclick = function () {
        if (confirm("Are you sure you want to delete this post?")) {
            button.closest('form').submit();
        }
    };
});