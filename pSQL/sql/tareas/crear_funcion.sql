create or replace FUNCTION comment_replies(id integer)
returns json
as
$$
declare result json;
BEGIN
    select json_agg(json_build_object('user', user_id, 'comment', content)) into result
    from comments
    where comment_parent_id=id;

    return result;
END;
$$
LANGUAGE plpgsql;

select comment_replies(comment_id)
from comments;