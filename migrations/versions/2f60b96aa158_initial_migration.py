"""Initial migration

Revision ID: 2f60b96aa158
Revises: 
Create Date: 2025-07-23 01:27:23.137411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f60b96aa158'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.Column('image1', sa.String(length=200), nullable=True),
    sa.Column('alttitle1', sa.String(length=100), nullable=True),
    sa.Column('image2', sa.String(length=200), nullable=True),
    sa.Column('alttitle2', sa.String(length=100), nullable=True),
    sa.Column('image3', sa.String(length=200), nullable=True),
    sa.Column('alttitle3', sa.String(length=100), nullable=True),
    sa.Column('link1', sa.String(length=200), nullable=True),
    sa.Column('link2', sa.String(length=200), nullable=True),
    sa.Column('frase1', sa.String(length=200), nullable=False),
    sa.Column('frase2', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
