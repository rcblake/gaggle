"""empty message

Revision ID: 71204a9b762c
Revises: 
Create Date: 2023-07-18 21:38:18.511801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71204a9b762c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trips',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('ticketed', sa.Boolean(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.id'], name=op.f('fk_events_trip_id_trips')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lodgings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.id'], name=op.f('fk_lodgings_trip_id_trips')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('travel_legs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('travel_type', sa.String(), nullable=True),
    sa.Column('departure_time', sa.DateTime(), nullable=False),
    sa.Column('arrival_time', sa.DateTime(), nullable=False),
    sa.Column('flight_number', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.id'], name=op.f('fk_travel_legs_trip_id_trips')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_travel_legs_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trip_tasks',
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
    sa.ForeignKeyConstraint(['trip_id'], ['trips.id'], name=op.f('fk_trip_tasks_trip_id_trips')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trip_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.id'], name=op.f('fk_trip_users_trip_id_trips'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_trip_users_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trip_users')
    op.drop_table('trip_tasks')
    op.drop_table('travel_legs')
    op.drop_table('lodgings')
    op.drop_table('events')
    op.drop_table('users')
    op.drop_table('trips')
    # ### end Alembic commands ###
