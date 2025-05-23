"""init_db

Revision ID: 023638268b63
Revises: 
Create Date: 2025-03-14 11:01:50.053945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import geoalchemy2
from geoalchemy2 import Geometry

# revision identifiers, used by Alembic.
revision: str = '023638268b63'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('digital_permit_annotation',
    sa.Column('objectid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('globalid', sa.String(length=38), nullable=False),
    sa.Column('formid', sa.String(length=38), nullable=True),
    sa.Column('templateid', sa.String(length=38), nullable=True),
    sa.Column('projectid', sa.String(length=38), nullable=True),
    sa.Column('annotation', sa.String(length=255), nullable=True),
    sa.Column('approval_status', sa.SmallInteger(), nullable=True),
    sa.Column('start_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.Column('end_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('gdb_geomattr_data', sa.LargeBinary(), nullable=True),
    sa.Column('shape', Geometry(geometry_type='POINTM', srid=3857, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.PrimaryKeyConstraint('objectid')
    )
    op.create_index(op.f('ix_digital_permit_annotation_globalid'), 'digital_permit_annotation', ['globalid'], unique=True)
    op.create_index(op.f('ix_digital_permit_annotation_objectid'), 'digital_permit_annotation', ['objectid'], unique=False)
    op.create_table('digital_permit_point',
    sa.Column('objectid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('globalid', sa.String(length=38), nullable=False),
    sa.Column('projectid', sa.String(length=38), nullable=True),
    sa.Column('templateid', sa.String(length=38), nullable=True),
    sa.Column('formid', sa.String(length=38), nullable=True),
    sa.Column('approval_status', sa.SmallInteger(), nullable=True),
    sa.Column('start_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.Column('end_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('gdb_geomattr_data', sa.LargeBinary(), nullable=True),
    sa.Column('shape', Geometry(geometry_type='POINTM', srid=3857, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.PrimaryKeyConstraint('objectid')
    )
    op.create_index(op.f('ix_digital_permit_point_globalid'), 'digital_permit_point', ['globalid'], unique=True)
    op.create_index(op.f('ix_digital_permit_point_objectid'), 'digital_permit_point', ['objectid'], unique=False)
    op.create_table('digital_permit_polygon',
    sa.Column('objectid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('globalid', sa.String(length=38), nullable=False),
    sa.Column('formid', sa.String(length=38), nullable=True),
    sa.Column('templateid', sa.String(length=38), nullable=True),
    sa.Column('projectid', sa.String(length=38), nullable=True),
    sa.Column('approval_status', sa.SmallInteger(), nullable=True),
    sa.Column('start_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.Column('end_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('gdb_geomattr_data', sa.LargeBinary(), nullable=True),
    sa.Column('shape', Geometry(geometry_type='POLYGONM', srid=3857, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.PrimaryKeyConstraint('objectid')
    )
    op.create_index(op.f('ix_digital_permit_polygon_globalid'), 'digital_permit_polygon', ['globalid'], unique=True)
    op.create_index(op.f('ix_digital_permit_polygon_objectid'), 'digital_permit_polygon', ['objectid'], unique=False)
    op.create_table('files',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('filename', sa.String(length=255), nullable=False),
    sa.Column('file_path', sa.String(length=255), nullable=False),
    sa.Column('mime_type', sa.String(length=100), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_files_id'), 'files', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('role', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_login', sa.DateTime(timezone=True), nullable=True),
    sa.Column('last_login_attempt', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_first_name'), 'users', ['first_name'], unique=False)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_last_name'), 'users', ['last_name'], unique=False)
    op.create_table('providers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('provider', sa.String(length=255), nullable=True),
    sa.Column('provider_id', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_providers_id'), 'providers', ['id'], unique=False)
    op.create_index(op.f('ix_providers_provider'), 'providers', ['provider'], unique=False)
    op.create_index(op.f('ix_providers_provider_id'), 'providers', ['provider_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_providers_provider_id'), table_name='providers')
    op.drop_index(op.f('ix_providers_provider'), table_name='providers')
    op.drop_index(op.f('ix_providers_id'), table_name='providers')
    op.drop_table('providers')
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_first_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_files_id'), table_name='files')
    op.drop_table('files')
    op.drop_index(op.f('ix_digital_permit_polygon_objectid'), table_name='digital_permit_polygon')
    op.drop_index(op.f('ix_digital_permit_polygon_globalid'), table_name='digital_permit_polygon')
    op.drop_table('digital_permit_polygon')
    op.drop_index(op.f('ix_digital_permit_point_objectid'), table_name='digital_permit_point')
    op.drop_index(op.f('ix_digital_permit_point_globalid'), table_name='digital_permit_point')
    op.drop_table('digital_permit_point')
    op.drop_index(op.f('ix_digital_permit_annotation_objectid'), table_name='digital_permit_annotation')
    op.drop_index(op.f('ix_digital_permit_annotation_globalid'), table_name='digital_permit_annotation')
    op.drop_table('digital_permit_annotation')
    # ### end Alembic commands ###
