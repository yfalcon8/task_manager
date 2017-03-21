// Your Client ID can be retrieved from your project in the Google
// Developer Console, https://console.developers.google.com
var CLIENT_ID = '608382298047-beqcvm6a4a98p55lr6uben0r5qc7ce3m.apps.googleusercontent.com';

$(document).ready(function() {
    console.log("ready!");

    $("form").on("submit", function() {
        console.log("the form has been submitted");

        var taskName = $('input[name="task_name"]').val();
        var taskPriorityElem = document.getElementById("task_priority");
        var taskPriority = taskPriorityElem.options[taskPriorityElem.selectedIndex].value;
        var taskFrequencyElem = document.getElementById("task_frequency");
        var taskFrequency = taskFrequencyElem.options[taskFrequencyElem.selectedIndex].value;
        var taskDate = $('input[name="task_date"]').val();

        var goalName = $('input[name="goal_name"]').val();
        var goalDate = $('input[name="goal_date"]').val();

        if (taskName) {
          console.log(taskName, taskPriority, taskFrequency, taskDate);
        } else {
          console.log(goalName, goalDate);
        }
    });
});
// var SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"];

/*Check the user authentication */

function checkAuth() {
  gapi.auth.authorize(
    {
      'client_id': CLIENT_ID,
      // 'scope': SCOPES.join(' '),
      'immediate': true
    }, handleAuthResult);
}

/* function for handling authorozation of server */

function handleAuthResult(authResult) {
  var authorizeDiv = document.getElementById('authorize-div');
  if (authResult && !authResult.error) {
    // Hide auth UI, then load client library.
    authorizeDiv.style.display = 'none';
    loadCalendarApi();
  } else {
    // Show auth UI, allowing the user to initiate authorization by
    // clicking authorize button.
    authorizeDiv.style.display = 'inline';
  }
}

  /*the response function to user click */

function handleAuthClick(event) {
  gapi.auth.authorize(
    {client_id: CLIENT_ID, immediate: false},
    handleAuthResult);
  return false;
}

   /*loading client library */

function loadCalendarApi() {
  gapi.client.load('calendar', 'v3', listUpcomingEvents);
}

     /*print out the results of users calendar response*/

function listUpcomingEvents() {
  var request = gapi.client.calendar.events.list({
    'calendarId': 'primary',
    'timeMin': (new Date()).toISOString(),
    'showDeleted': false,
    'singleEvents': true,
    'maxResults': 15,
    'orderBy': 'startTime'
  });

  request.execute(function(resp) {
    var events = resp.items;
    appendPre('The up comming events in your calendar are:'+ '\n'+'\n');



    if (events.length > 0) {
      for (i = 0; i < events.length; i++) {

        var event = events[i];
        var when = event.start.dateTime;

        if (!when) {
          when = event.start.date;
        }
        appendPre(i+1+' '+ event.summary + ' ('+' '+ when +' '+ ')' + '\n');
      }
    } else {
      appendPre('No upcoming events found.');
    }

  });
}

    /* this will return the out put to body as its next node */

function appendPre(message) {
  var pre = document.getElementById('output');
  var textContent = document.createTextNode(message + '\n');
  pre.appendChild(textContent);
}