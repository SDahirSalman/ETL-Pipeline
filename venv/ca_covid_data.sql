CREATE TABLE IF NOT EXISTS "$OWNER/$REPO"."users_answers" (
  user_id INT,
  number_of_answers TEXT
);

TRUNCATE TABLE "$OWNER/$REPO"."users_answers";

INSERT INTO "$OWNER/$REPO"."users_answers"
  SELECT
  a.owner_user_id, COUNT(1) AS number_of_answers
   FROM "$OWNER/$REPO"."posts_questions" AS q 
   INNER JOIN "$OWNER/$REPO"."posts_answers" as a
   ON q.id = a.parent_id 
   WHERE q.tags LIKE %bigquery% 
   GROUP BY q.owner_user_id
   ORDER BY number_of_answers DESC;
 ;