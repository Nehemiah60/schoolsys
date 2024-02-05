"""empty message

Revision ID: 62e1bd7aa2ce
Revises: 717faf1d663f
Create Date: 2024-02-05 12:27:03.630905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62e1bd7aa2ce'
down_revision = '717faf1d663f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('teachers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('joined_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('teachers', schema=None) as batch_op:
        batch_op.drop_column('joined_date')

    # ### end Alembic commands ###
