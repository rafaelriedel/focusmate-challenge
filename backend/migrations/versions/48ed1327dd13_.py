"""Inserts some data.

Revision ID: 48ed1327dd13
Revises: 0b38c59afc12
Create Date: 2021-06-27 19:06:15.142116

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '48ed1327dd13'
down_revision = '0b38c59afc12'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """INSERT INTO users
    (email, first_name, last_name, date_created, active, confirmed, date_confirmed, hash_password)
    VALUES
    ('gandalf@middle-earth.net', 'Gandalf', 'The Grey', '2021-06-26 09:00:00', true, true, '2021-06-26 09:00:00', null)"""
    )

    op.execute(
        """INSERT INTO users
    (email, first_name, last_name, date_created, active, confirmed, date_confirmed, hash_password)
    VALUES
    ('frodo@theshire.org', 'Frodo', 'Baggings', '2021-06-26 09:00:00', true, true, '2021-06-26 09:00:00', null)"""
    )

    op.execute(
        """INSERT INTO users
    (email, first_name, last_name, date_created, active, confirmed, date_confirmed, hash_password)
    VALUES
    ('samwise@theshire.org', 'Samwise', 'Gamgee', '2021-06-26 09:00:00', true, true, '2021-06-26 09:00:00', null)"""
    )


def downgrade():
    pass
