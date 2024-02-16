document.addEventListener('DOMContentLoaded', function () {
    const csrftoken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
    // Handle the create milestone form
    document.getElementById('create-milestone-form').addEventListener('submit', function (e) {
        e.preventDefault();
        const milestoneTitle = document.getElementById('milestone-title').value;
        const milestoneContent = document.getElementById('milestone-content').value;
        console.log('Title:', milestoneTitle);
        console.log('Content:', milestoneContent);

        const formData = new FormData();
        formData.append('title', milestoneTitle);
        formData.append('content', milestoneContent);

        fetch('/create_milestone/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrftoken,
                'X-Requested-With': 'XMLHttpRequest',
            },
            credentials: 'include', // Include cookies in the request
        })
        .then((response) => response.json())
        .then((data) => {
            console.log('Response Data:', data);

            if (data.success) {
            // Entry created successfully, update the view
            const milestoneSection = document.getElementById('milestone-section');
            const newMilestone = document.createElement('li');
            newMilestone.className = 'milestone';

            // Create elements for the title and content
            const titleElement = document.createElement('h4');
            titleElement.textContent = data.title;
            const contentElement = document.createElement('p');
            contentElement.textContent = data.content;

            // Append the title and content to the milestone list item
            newMilestone.appendChild(titleElement);
            newMilestone.appendChild(contentElement);

            milestoneSection.appendChild(newMilestone);

                // Reload the page
                location.reload();

            } else {
                alert('Error creating a milestone: ' + data.error_message);
            }
        })
        .catch((error) => {
            console.log('Error:', error);
            alert('Error creating a milestone.');
        });
    });
});
