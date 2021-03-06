"""hello

Revision ID: ecea0fc7887d
Revises: 8093374dc5d4
Create Date: 2020-05-19 00:37:36.731699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecea0fc7887d'
down_revision = '8093374dc5d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'title',
               existing_type=sa.VARCHAR(length=100))
    op.alter_column('post', 'user_id',
               existing_type=sa.INTEGER())
    op.alter_column('post', 'verified',
               existing_type=sa.BOOLEAN())
    op.create_index(op.f('ix_post_start_time'), 'post', ['start_time'], unique=False)
    op.create_index(op.f('ix_post_title'), 'post', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_title'), table_name='post')
    op.drop_index(op.f('ix_post_start_time'), table_name='post')
    op.alter_column('post', 'verified',
               existing_type=sa.BOOLEAN())
    op.alter_column('post', 'user_id',
               existing_type=sa.INTEGER())
    op.alter_column('post', 'title',
               existing_type=sa.VARCHAR(length=100))
    # ### end Alembic commands ###
