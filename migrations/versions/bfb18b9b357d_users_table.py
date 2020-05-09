"""users table

Revision ID: bfb18b9b357d
Revises: 
Create Date: 2020-05-09 22:55:38.978415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfb18b9b357d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('email', sa.String(length=128), nullable=False))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.drop_index('ix_user_Email', table_name='user')
    op.drop_column('user', 'Email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('Email', sa.VARCHAR(length=128), nullable=False))
    op.create_index('ix_user_Email', 'user', ['Email'], unique=1)
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'email')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
