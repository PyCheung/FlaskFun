"""initial migration

Revision ID: 6187a5080cd9
Revises: 0adf04f347fb
Create Date: 2017-01-20 19:42:23.264034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6187a5080cd9'
down_revision = '0adf04f347fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Flaskusers', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('Flaskusers', sa.Column('last_login', sa.DateTime(), nullable=True))
    op.add_column('Flaskusers', sa.Column('member_since', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Flaskusers', 'member_since')
    op.drop_column('Flaskusers', 'last_login')
    op.drop_column('Flaskusers', 'about_me')
    # ### end Alembic commands ###
