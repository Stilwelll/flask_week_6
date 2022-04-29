"""'third'

Revision ID: 94f00d41e743
Revises: 65f2cd2a8c23
Create Date: 2022-04-29 03:51:37.861713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94f00d41e743'
down_revision = '65f2cd2a8c23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('itemname', sa.String(length=30), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('phone_book')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phone_book',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=14), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='phone_book_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='phone_book_pkey')
    )
    op.drop_table('item')
    # ### end Alembic commands ###