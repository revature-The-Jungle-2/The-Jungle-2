// login
insert into jungle_user values(default, 'Dean', 'Winchester', 'ghosthunter', 'impala', default, '10/01/1977', 'image', default, default);
insert into jungle_user values(default, 'Sam', 'Winchester', 'vampirehunter', 'impala', default, '10/01/1980', 'image', default, default);
insert into jungle_user values(default, 'John', 'Winchester', 'werewolfhunter', 'impala', default, '10/01/1957', 'image', default, default);

// chat
insert into user_table values(10000, 'first name', 'last name', 'email', 'username', 'passcode', null, now(), null);
insert into group_table values(10000, 10000, 'group name');
insert into chat_log_table values(10000, now(), 10000, 10000,'hello world');
insert into chat_log_table values(10001, now() - interval '3 minutes', 10000, 10000, 'hello world');
