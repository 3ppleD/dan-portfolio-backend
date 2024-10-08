"""empty message

Revision ID: e65a6f3e79c4
Revises: 81cb26b5ca2a
Create Date: 2024-08-23 15:09:20.571686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e65a6f3e79c4'
down_revision = '81cb26b5ca2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('about', schema=None) as batch_op:
        batch_op.alter_column('skills',
               existing_type=sa.TEXT(),
               type_=sa.String(length=1000),
               existing_nullable=True)

    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.alter_column('description1',
               existing_type=sa.VARCHAR(length=1000),
               nullable=True)
        batch_op.alter_column('description2',
               existing_type=sa.VARCHAR(length=1000),
               nullable=True)
        batch_op.alter_column('link',
               existing_type=sa.VARCHAR(length=1000),
               nullable=True)
        batch_op.alter_column('technologies',
               existing_type=sa.VARCHAR(length=5000),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.alter_column('technologies',
               existing_type=sa.VARCHAR(length=5000),
               nullable=False)
        batch_op.alter_column('link',
               existing_type=sa.VARCHAR(length=1000),
               nullable=False)
        batch_op.alter_column('description2',
               existing_type=sa.VARCHAR(length=1000),
               nullable=False)
        batch_op.alter_column('description1',
               existing_type=sa.VARCHAR(length=1000),
               nullable=False)

    with op.batch_alter_table('about', schema=None) as batch_op:
        batch_op.alter_column('skills',
               existing_type=sa.String(length=1000),
               type_=sa.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###
