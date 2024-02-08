"""empty message

Revision ID: 8396da4f1fcc
Revises: 32d4ef023a6e
Create Date: 2024-02-08 11:56:26.802910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8396da4f1fcc'
down_revision = '32d4ef023a6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grade', schema=None) as batch_op:
        batch_op.add_column(sa.Column('levels', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grade', schema=None) as batch_op:
        batch_op.drop_column('levels')

    # ### end Alembic commands ###
