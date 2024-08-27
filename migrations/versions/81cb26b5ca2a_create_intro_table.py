"""Create intro table

Revision ID: 81cb26b5ca2a
Revises: 
Create Date: 2024-08-23 14:21:22.008548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81cb26b5ca2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('about',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lottieURL', sa.String(length=1000), nullable=True),
    sa.Column('description1', sa.String(length=1000), nullable=False),
    sa.Column('description2', sa.String(length=1000), nullable=False),
    sa.Column('skills', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=100), nullable=False),
    sa.Column('mobile', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('experience',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('period', sa.String(length=100), nullable=False),
    sa.Column('company', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('intro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('welcomeText', sa.String(length=1000), nullable=False),
    sa.Column('firstName', sa.String(length=100), nullable=False),
    sa.Column('lastName', sa.String(length=100), nullable=False),
    sa.Column('caption', sa.String(length=10000), nullable=False),
    sa.Column('description', sa.String(length=10000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description1', sa.String(length=1000), nullable=False),
    sa.Column('description2', sa.String(length=1000), nullable=False),
    sa.Column('img_url', sa.String(length=1000), nullable=True),
    sa.Column('link', sa.String(length=1000), nullable=False),
    sa.Column('technologies', sa.String(length=5000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    op.drop_table('intro')
    op.drop_table('experience')
    op.drop_table('contact')
    op.drop_table('about')
    # ### end Alembic commands ###
