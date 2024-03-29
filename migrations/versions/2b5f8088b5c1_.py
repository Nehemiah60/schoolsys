"""empty message

Revision ID: 2b5f8088b5c1
Revises: 5f9407105453
Create Date: 2024-02-01 08:14:01.628790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b5f8088b5c1'
down_revision = '5f9407105453'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'students', ['student_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fees', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('student_id')

    # ### end Alembic commands ###
