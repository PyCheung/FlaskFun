"""initial migration

Revision ID: 528f045d92d9
Revises: 6adf888a1d77
Create Date: 2017-01-30 19:10:59.680560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '528f045d92d9'
down_revision = '6adf888a1d77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['Flaskusers.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['Flaskusers.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follows')
    # ### end Alembic commands ###