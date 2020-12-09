# Migrating SAD CMS Site PostgreSQL Databases from 9.2 to 13.1

This is a comprehensive replacement of the databse, not an upgrade.

## A) BACKUP EXISTING DATABASE

1. ssh into host
2. become sudo: `sudo su`
3. become postgres user: `sudo su - postgres`
4. dump the database:  `pg_dumpall > ~/DB_BACKUP_FILE.sql`
    - Note: use a descriptive name for the dump file (eg. `texascale_org_prod_20201204.sql`).
5. move the backup to the `/tmp` folder for now: ` mv DB_BACKUP_FILE.sql /tmp/`

## B) UPDATE THE HOST 

1. ssh into host
2. become sudo: `sudo su`
3. update all packages: `yum update -y`
- NOTE: Servers running the old SAD configuration will need to also install the new ldap modules: `sudo yum install python-devel openldap-devel -y`
4. reboot the system to let kernel updates take effect: `reboot now`

## C) DISABLE THE OLD POSTGRESQL 9.2 DATABASE

1. ssh into host
2. become sudo: `sudo su`
3. disable OLD databese service: `systemctl disable postgresql`

## D) INSTALL & INITIALIZE THE NEW POSTGRESQL 13.1 DATABASE

1. ssh into host
2. become sudo: `sudo su`
3. add repo for packages: `yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm`
4. install packages: `yum -y install postgresql13 postgresql13-server`
5. intialize database: `/usr/pgsql-13/bin/postgresql-13-setup initdb`
6. Edit the `pg_hba.conf` file for the correct server IP and method types:  `vim /var/lib/pgsql/13/data/pg_hba.conf`
7. start database service: `systemctl start postgresql-13`
8. check database status: `systemctl status postgresql-13`
9. set service to autorun as host reboot: `systemctl enable postgresql-13`
10. Reboot the server: `sudo reboot now`

### pg_hba.conf example:

```
# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
#local   all             all                                     peer
#local	 all		     all					                 md5
local	all		        all					                    trust

# Accept from anywhere (development and testing use ONLY!).
host    all             all             0.0.0.0/0               md5
# Accept from trusted subnet (production setting).
# UPDATE SERVER IP TO REFLECT HOST.
host    all             all             129.114.60.24/24        md5

# IPv4 local connections:
#host    all             all             127.0.0.1/32            scram-sha-256
host	all		        all		        127.0.0.1/32		    md5

# IPv6 local connections:
#host    all             all             ::1/128                 scram-sha-256
host	all		        all		        ::1/128			md5

# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     peer
#host    replication     all             127.0.0.1/32            scram-sha-256
host	repliction	    all		        127.0.0.1/32		    md5
#host    replication     all             ::1/128                 scram-sha-256
host	replication	    all		        ::1/128			        md5
```

## E) RESTORE DATA TO NEW DB

1. ssh into host
2. become sudo: `sudo su`
3. verify the database is running: `systemctl status postgresql-13`
4. become postgres user: `sudo su - postgres`
5. restore the database dump: `psql --set ON_ERROR_STOP=on -f /tmp/DB_BACKUP_FILE.sql`
- NOTE: if you encounter errors during the restore, check that the correct password has been applied to the postgresadmin user (compare to the value in `/srv/taccsite/taccsite_cms/secrets.py`).
6. start psql: `psql`
7. verify the database exists with the correct users: `\l`
8. verify the users exist: `\du`
9. apply roles to postgresadmin user: `ALTER ROLE postgresadmin WITH CREATEDB CREATEROLE INHERIT LOGIN REPLICATION;`
10. verify the users exist with the correct roles granted: `\du`
11. connect to the database: `\c taccsite`
12. verify that the database is populated with the expected tables: `\dt`
13. exit psql: `\q`

## F) RESUME STEPS FOR USING CMS BRANCH AND SUBMODULE

Steps for the subsequent actions can be found here: (get notes for this from Wesley)
