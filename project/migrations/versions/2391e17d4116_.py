"""empty message

Revision ID: 2391e17d4116
Revises: 
Create Date: 2024-06-24 07:25:26.424227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2391e17d4116'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(length=50), nullable=True),
    sa.Column('final_price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('password_confirm', sa.String(length=50), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('product')
    # ### end Alembic commands ###
