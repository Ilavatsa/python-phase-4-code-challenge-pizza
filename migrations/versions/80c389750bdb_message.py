"""message

Revision ID: 80c389750bdb
Revises: 2a8a0288fd16
Create Date: 2023-07-07 10:21:11.111111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80c389750bdb'
down_revision = '2a8a0288fd16'
branch_labels = None
depends_on = None


def upgrade():
    # Check if the table exists before creating it
    if not _table_exists('restaurants'):
        op.create_table('restaurants',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(length=255), nullable=False),
            sa.PrimaryKeyConstraint('id', name=op.f('pk_restaurants'))
        )

    # Check if the table exists before creating it
    if not _table_exists('pizzas'):
        op.create_table('pizzas',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(length=255), nullable=False),
            sa.PrimaryKeyConstraint('id', name=op.f('pk_pizzas'))
        )


def downgrade():
    op.drop_table('pizzas')
    op.drop_table('restaurants')


def _table_exists(table_name):
    # Check if the table exists in the current database schema
    bind = op.get_bind()
    return bind.dialect.has_table(bind, table_name)




