"""empty message

Revision ID: 2a8a0288fd16
Revises: 
Create Date: 2024-06-30 16:50:05.649285

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = '2a8a0288fd16'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Get the connection and create an Inspector
    bind = op.get_bind()
    inspector = Inspector.from_engine(bind)
    
    # Check if the 'pizzas' table exists before creating it
    if not inspector.has_table('pizzas'):
        op.create_table(
            'pizzas',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String()),
            sa.Column('ingredients', sa.String())
        )
    
    # Check if the 'restaurants' table exists before creating it
    if not inspector.has_table('restaurants'):
        op.create_table(
            'restaurants',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(), nullable=True),
            sa.Column('address', sa.String(), nullable=True),
            sa.PrimaryKeyConstraint('id')
        )
    
    # Check if the 'restaurant_pizzas' table exists before creating it
    if not inspector.has_table('restaurant_pizzas'):
        op.create_table(
            'restaurant_pizzas',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('price', sa.Integer(), nullable=False),
            sa.PrimaryKeyConstraint('id')
        )

def downgrade():
    # Drop tables in reverse order of creation
    op.drop_table('restaurant_pizzas')
    op.drop_table('restaurants')
    op.drop_table('pizzas')
