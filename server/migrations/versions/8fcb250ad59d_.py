"""empty message

Revision ID: 8fcb250ad59d
Revises: 62533ff109a0
Create Date: 2023-07-18 21:52:47.792223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fcb250ad59d'
down_revision = '62533ff109a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('note', sa.String(), nullable=False),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('optional', sa.Boolean(), nullable=True),
    sa.Column('everyone', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.id'], name=op.f('fk_tasks_trip_id_trips')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('trip_tasks')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trip_tasks',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('trip_id', sa.INTEGER(), nullable=True),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('note', sa.VARCHAR(), nullable=False),
    sa.Column('link', sa.VARCHAR(), nullable=True),
    sa.Column('cost', sa.FLOAT(), nullable=True),
    sa.Column('optional', sa.BOOLEAN(), nullable=True),
    sa.Column('everyone', sa.BOOLEAN(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.id'], name='fk_trip_tasks_trip_id_trips'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('tasks')
    # ### end Alembic commands ###
