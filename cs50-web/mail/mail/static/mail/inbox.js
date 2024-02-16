document.addEventListener('DOMContentLoaded', function () {
    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);

    // By default, load the inbox
    load_mailbox('inbox');
  });

  function compose_email(recipient, subject, body) {
    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Pre-fill the composition fields if arguments are provided
    document.querySelector('#compose-recipients').value = recipient ? `${recipient}` : '';
    document.querySelector('#compose-subject').value = subject ? `Re: ${subject}` : '';
    document.querySelector('#compose-body').value = body ? `${body}` : '';

    // Define the event listener function
    function submitForm(event) {
      event.preventDefault();

      // Get form data
      const recipients = document.querySelector('#compose-recipients').value;
      const subject = document.querySelector('#compose-subject').value;
      const body = document.querySelector('#compose-body').value;

      // Make a POST request to send the email
      fetch('/emails', {
        method: 'POST',
        body: JSON.stringify({
          recipients: recipients,
          subject: subject,
          body: body
        })
      })
        .then(response => response.json())
        .then(data => {
          // Handle the response here
          console.log(data);

          // Load the sent mailbox
          load_mailbox('sent');

          // Remove the event listener to prevent multiple submissions
          document.querySelector('#compose-form').removeEventListener('submit', submitForm);
        });
    }
    // Attach the event listener to the form
    document.querySelector('#compose-form').addEventListener('submit', submitForm);
}

function load_mailbox(mailbox) {
    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';

    // Add the mailbox name and header structure
    const emailsView = document.querySelector('#emails-view');
    emailsView.innerHTML = `
        <h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>
        <div class="email-header">
        <strong>Sender</strong> - <strong>Subject</strong> - <strong>Timestamp</strong>
        </div>
    `;

    // Fetch and display emails
    fetch(`/emails/${mailbox}`)
      .then(response => response.json())
      .then(emails => {
        // Handle the emails data here
        const emailsView = document.querySelector('#emails-view');

        emails.forEach(email => {
          const emailBox = document.createElement('div');
          emailBox.className = `email-item ${email.read ? 'read' : 'unread'}`;
          emailBox.innerHTML = `
            <strong>${email.sender}</strong> - ${email.subject} - ${email.timestamp}
          `;
          emailBox.addEventListener('click', function () {
            view_email(email.id, mailbox); // Pass the mailbox type to view_email
          });

          // Add event listener for archive/unarchive button (conditionally)
          if (mailbox === 'inbox' || mailbox === 'archive') {
            const archiveButton = document.createElement('button');
            archiveButton.className = 'archive-button';
            archiveButton.innerHTML = email.archived ? 'Unarchive' : 'Archive';
            archiveButton.addEventListener('click', function (event) {
              event.stopPropagation(); // Prevent the click from triggering the email click
              archive_email(email.id, email.archived);
            });
            emailBox.appendChild(archiveButton);
          }

          emailsView.appendChild(emailBox);
        });
      });
  }

  function view_email(email_id, mailbox) {
    // Fetch the email details
    fetch(`/emails/${email_id}`)
      .then(response => response.json())
      .then(email => {
        // Handle the email data here
        const emailView = document.querySelector('#emails-view');
        emailView.innerHTML = ''; // Clear the existing content

        const emailDetails = document.createElement('div');
        emailDetails.innerHTML = `
          <strong>From:</strong> ${email.sender}<br>
          <strong>To:</strong> ${email.recipients.join(', ')}<br>
          <strong>Subject:</strong> ${email.subject}<br>
          <strong>Timestamp:</strong> ${email.timestamp}<br>
          <strong>Body:</strong><br>${email.body}
        `;
        emailView.appendChild(emailDetails);

        // Mark the email as read
        mark_email_as_read(email_id);

        // Add event listener for reply button
        const replyButton = document.createElement('button');
        replyButton.className = 'reply-button';
        replyButton.innerHTML = 'Reply';
        replyButton.addEventListener('click', function () {
          // Pre-fill the email composition form
          const recipients = [email.sender]; // Use the sender as the recipient
          const subject = email.subject;
          const body = `On ${email.timestamp} ${email.sender} wrote:\n${email.body}`;
          compose_email(recipients, subject, body);
        });
        emailView.appendChild(replyButton);

        // Add event listener for archive/unarchive button (conditionally)
        if (mailbox === 'inbox' || mailbox === 'archive') {
          const archiveButton = document.createElement('button');
          archiveButton.className = 'archive-button';
          archiveButton.innerHTML = email.archived ? 'Unarchive' : 'Archive';
          archiveButton.addEventListener('click', function () {
            archive_email(email.id, email.archived);
          });
          emailView.appendChild(archiveButton);
        }
      });
  }


function archive_email(email_id, is_archived) {
    // Toggle the archived status
    const newArchivedStatus = !is_archived;

    // Send a PUT request to update the archived status
    fetch(`/emails/${email_id}`, {
      method: 'PUT',
      body: JSON.stringify({
        archived: newArchivedStatus
      })
    })
      .then(response => {
        if (response.status === 204) {
          // Successful PUT request with no content (empty response)
          console.log("Email archived/unarchived successfully.");
          load_mailbox('inbox'); // Reload the mailbox
        } else {
          throw new Error(`Unexpected response status: ${response.status}`);
        }
      })
      .catch(error => {
        console.error("Error archiving/unarchiving email:", error);
      });
  }

function mark_email_as_read(email_id) {
    // Send a PUT request to mark the email as read
    fetch(`/emails/${email_id}`, {
      method: 'PUT',
      body: JSON.stringify({
        read: true
      })
    })
      .then(response => {
        if (response.status === 204) {
          // Successful PUT request with no content (empty response)
          console.log("Email marked as read successfully.");
        } else {
          throw new Error(`Unexpected response status: ${response.status}`);
        }
      })
      .catch(error => {
        console.error("Error marking email as read:", error);
      });
  }
