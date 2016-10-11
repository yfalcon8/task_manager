INSERT INTO users (username, password, profile_img, email, time_zone)
VALUES ('Minnie', 'MouseGal', 'static/img/minnie.jpg', 'minnie@mouse.purr', 'PST'),
('LadyFlash', 'PowerfulLady', 'static/img/ladyflash.jpg', 'lady@flash.pow', 'PST');

INSERT INTO tasks (task_name, due_date, priority, open_close_status, task_frequency, taskcat_name)
VALUES ('Do laundry', '10/31/16', 5, 1, 'weekly', 'personal');

INSERT INTO goals (user_id, description, active_goal, time_toachieve, goalcat_name)
VALUES (1, 'Be a better communicator', 'True', 'month', 'professional');