"""empty message

Revision ID: 3bda3a710eb
Revises: 4175dff441
Create Date: 2014-07-18 14:46:20.665598

"""

# revision identifiers, used by Alembic.
revision = '3bda3a710eb'
down_revision = '4175dff441'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sponsors', sa.Column('payment_received', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sponsors', 'payment_received')
    ### end Alembic commands ###