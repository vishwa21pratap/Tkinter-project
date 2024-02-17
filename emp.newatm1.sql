create database emp_rec;
use emp_rec ; 
create table emp_rec
(
Empid varchar(50),
Accnumber varchar(50) not null,
Cusname varchar(50),
Balance varchar(50),
Gender varchar(20),
Open_date varchar(20),
primary key (Empid)
);
select *from emp_rec;
insert into emp_rec values("12131",000012346500,"Vivek Yadav","5000000","Male",'2021-04-01');
insert into emp_rec values("12321",000012346600,"Ajay kannaujiya","50000","Male",'2021-04-01');
insert into emp_rec values("14621",000012346700,"Vijay Kumar","50000","Male",'2021-04-02');
insert into emp_rec values("24321",000012346800,"Ankush Verma","1000000","Male",'2021-04-02');
insert into emp_rec values("42612",000012346900,"Vikas Dube ","2000000","Male",'2021-04-03');
insert into emp_rec values("23141",000012347000,"Riya Yadav ","50000","female",'2021-04-04');
insert into emp_rec values("86214",000012347100,"Lakshmi Sinha ","1000000","female",'2021-04-05');
insert into emp_rec values("62121",000012347200,"Prachi Singh ","1000000","female",'2021-04-05');
insert into emp_rec values("41512",000012347300," Tanu Yadav","2000000","female",'2021-04-06');
insert into emp_rec values("21212",000012347400," Ankita Sharma","60000","female",'2021-04-11');
use emp_rec
desc emp_rec;