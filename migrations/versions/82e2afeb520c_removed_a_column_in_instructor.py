"""removed a column in Instructor

Revision ID: 82e2afeb520c
Revises: cd045283930b
Create Date: 2018-01-12 01:40:12.052484

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '82e2afeb520c'
down_revision = 'cd045283930b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('instructor', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('instructor', sa.Column('test', mysql.VARCHAR(length=1), nullable=True))
    # ### end Alembic commands ###
