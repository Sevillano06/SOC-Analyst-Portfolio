CREATE TABLE login_logs (
    id INt PRIMARY KEY,
    fecha DATETIME,
    usuario VARCHAR(50),
    ip VARCHAR(20),
    estado VARCHAR(20)
);

SELECT * FROM login_logs;

Select count(*) FROM login_logs;

select * from login_logs where  estado = 'Failed';

Select usuario , count(*) as total_fallidos 
from login_logs
where estado = 'Falied'
group by usuario; 



Select ip, count(*) as aparaciones 
From login_logs
group by ip
order by aparaciones desc 
limit 1 ; 