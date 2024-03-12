from aplicacion.dto import ContratoDTO


class MapeadorContratoDTOJson():
    def externo_a_dto(self, externo: dict) -> ContratoDTO:
        contrato_dto = ContratoDTO()
        contrato_dto.ciudad = externo.get('ciudad')   
        contrato_dto.departamento = externo.get('departamento')   
        contrato_dto.direccion = externo.get('direccion')   
        contrato_dto.email_contacto = externo.get('email_contacto')   
        contrato_dto.documento_identidad_numero_identificacion = externo.get('documento_identidad_numero_identificacion')   
        contrato_dto.documento_identidad_tipo = externo.get('documento_identidad_tipo')
        contrato_dto.estado_compania = externo.get('estado_compania')   
        contrato_dto.latitud = externo.get('latitud') 
        contrato_dto.longitud = externo.get('longitud') 
        contrato_dto.nombre_compania = externo.get('nombre_compania') 
        contrato_dto.pais = externo.get('pais') 
        contrato_dto.representante_legal = externo.get('representante_legal') 
        contrato_dto.telefono_contacto = externo.get('telefono_contacto') 
        contrato_dto.tipo_industria = externo.get('tipo_industria') 
        contrato_dto.nombre_propiedad = externo.get('nombre_propiedad') 
        contrato_dto.tipo_propiedad = externo.get('tipo_propiedad') 
        contrato_dto.codigo_postal = externo.get('codigo_postal') 
        contrato_dto.area_lote = externo.get('area_lote') 
        contrato_dto.estrato_socioeconomico = externo.get('estrato_socioeconomico') 
        contrato_dto.valor_venta = externo.get('valor_venta') 
        contrato_dto.valor_arriendo_mensual = externo.get('valor_arriendo_mensual') 
        contrato_dto.moneda = externo.get('moneda') 
        contrato_dto.propietario = externo.get('propietario') 
        contrato_dto.estado = externo.get('estado')   
        contrato_dto.arrendatario = externo.get('arrendatario') 
        contrato_dto.fecha_ultimo_contrato = externo.get('fecha_ultimo_contrato') 
        contrato_dto.fecha_expiracion_contrato_actual = externo.get('fecha_expiracion_contrato_actual') 
        contrato_dto.fecha_inicio = externo.get('fecha_inicio') 
        contrato_dto.fecha_fin = externo.get('fecha_fin') 
        contrato_dto.fecha_ejecucion = externo.get('fecha_ejecucion') 
        contrato_dto.monto = externo.get('monto') 
        contrato_dto.tipo = externo.get('tipo') 
        return contrato_dto
    
    def dto_a_externo(self, dto: ContratoDTO) -> dict:
        return dto.__dict__