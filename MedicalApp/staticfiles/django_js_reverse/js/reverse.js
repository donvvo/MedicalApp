this.Urls=(function(){var Urls={};var self={url_patterns:{}};var _get_url=function(url_pattern){return function(){var _arguments,index,url,url_arg,url_args,_i,_len,_ref,_ref_list,match_ref,provided_keys,build_kwargs;_arguments=arguments;_ref_list=self.url_patterns[url_pattern];if(arguments.length==1&&typeof(arguments[0])=="object"){var provided_keys_list=Object.keys(arguments[0]);provided_keys={};for(_i=0;_i<provided_keys_list.length;_i++)
provided_keys[provided_keys_list[_i]]=1;match_ref=function(ref)
{var _i;if(ref[1].length!=provided_keys_list.length)
return false;for(_i=0;_i<ref[1].length&&ref[1][_i]in provided_keys;_i++);return _i==ref[1].length;}
build_kwargs=function(keys){return _arguments[0];}}else{match_ref=function(ref)
{return ref[1].length==_arguments.length;}
build_kwargs=function(keys){var kwargs={};for(var i=0;i<keys.length;i++){kwargs[keys[i]]=_arguments[i];}
return kwargs;}}
for(_i=0;_i<_ref_list.length&&!match_ref(_ref_list[_i]);_i++);if(_i==_ref_list.length)
return null;_ref=_ref_list[_i];url=_ref[0],url_args=build_kwargs(_ref[1]);for(url_arg in url_args){url=url.replace("%("+url_arg+")s",url_args[url_arg]||'');}
return'/'+url;};};var name,pattern,self,url_patterns,_i,_len,_ref;url_patterns=[['about',[['about/',[]]],],['account_change_password',[['accounts/password/change/',[]]],],['account_confirm_email',[['accounts/confirm\u002Demail/%(key)s/',['key',]]],],['account_email',[['accounts/email/',[]]],],['account_email_verification_sent',[['accounts/confirm\u002Demail/',[]]],],['account_inactive',[['accounts/inactive/',[]]],],['account_login',[['accounts/login/',[]]],],['account_logout',[['accounts/logout/',[]]],],['account_reset_password',[['accounts/password/reset/',[]]],],['account_reset_password_done',[['accounts/password/reset/done/',[]]],],['account_reset_password_from_key',[['accounts/password/reset/key/%(uidb36)s\u002D%(key)s/',['uidb36','key',]]],],['account_reset_password_from_key_done',[['accounts/password/reset/key/done/',[]]],],['account_set_password',[['accounts/password/set/',[]]],],['account_signup',[['accounts/signup/',[]]],],['admin:MedicalAppointments_clinic_add',[['admin/MedicalAppointments/clinic/add/',[]]],],['admin:MedicalAppointments_clinic_change',[['admin/MedicalAppointments/clinic/%(_0)s/',['_0',]]],],['admin:MedicalAppointments_clinic_changelist',[['admin/MedicalAppointments/clinic/',[]]],],['admin:MedicalAppointments_clinic_delete',[['admin/MedicalAppointments/clinic/%(_0)s/delete/',['_0',]]],],['admin:MedicalAppointments_clinic_history',[['admin/MedicalAppointments/clinic/%(_0)s/history/',['_0',]]],],['admin:MedicalAppointments_doctor_add',[['admin/MedicalAppointments/doctor/add/',[]]],],['admin:MedicalAppointments_doctor_change',[['admin/MedicalAppointments/doctor/%(_0)s/',['_0',]]],],['admin:MedicalAppointments_doctor_changelist',[['admin/MedicalAppointments/doctor/',[]]],],['admin:MedicalAppointments_doctor_delete',[['admin/MedicalAppointments/doctor/%(_0)s/delete/',['_0',]]],],['admin:MedicalAppointments_doctor_history',[['admin/MedicalAppointments/doctor/%(_0)s/history/',['_0',]]],],['admin:MedicalAppointments_doctorspecialty_add',[['admin/MedicalAppointments/doctorspecialty/add/',[]]],],['admin:MedicalAppointments_doctorspecialty_change',[['admin/MedicalAppointments/doctorspecialty/%(_0)s/',['_0',]]],],['admin:MedicalAppointments_doctorspecialty_changelist',[['admin/MedicalAppointments/doctorspecialty/',[]]],],['admin:MedicalAppointments_doctorspecialty_delete',[['admin/MedicalAppointments/doctorspecialty/%(_0)s/delete/',['_0',]]],],['admin:MedicalAppointments_doctorspecialty_history',[['admin/MedicalAppointments/doctorspecialty/%(_0)s/history/',['_0',]]],],['admin:MedicalAppointments_patient_add',[['admin/MedicalAppointments/patient/add/',[]]],],['admin:MedicalAppointments_patient_change',[['admin/MedicalAppointments/patient/%(_0)s/',['_0',]]],],['admin:MedicalAppointments_patient_changelist',[['admin/MedicalAppointments/patient/',[]]],],['admin:MedicalAppointments_patient_delete',[['admin/MedicalAppointments/patient/%(_0)s/delete/',['_0',]]],],['admin:MedicalAppointments_patient_history',[['admin/MedicalAppointments/patient/%(_0)s/history/',['_0',]]],],['admin:MedicalForms_general_add',[['admin/MedicalForms/general/add/',[]]],],['admin:MedicalForms_general_change',[['admin/MedicalForms/general/%(_0)s/',['_0',]]],],['admin:MedicalForms_general_changelist',[['admin/MedicalForms/general/',[]]],],['admin:MedicalForms_general_delete',[['admin/MedicalForms/general/%(_0)s/delete/',['_0',]]],],['admin:MedicalForms_general_history',[['admin/MedicalForms/general/%(_0)s/history/',['_0',]]],],['admin:MedicalForms_healthhistory_add',[['admin/MedicalForms/healthhistory/add/',[]]],],['admin:MedicalForms_healthhistory_change',[['admin/MedicalForms/healthhistory/%(_0)s/',['_0',]]],],['admin:MedicalForms_healthhistory_changelist',[['admin/MedicalForms/healthhistory/',[]]],],['admin:MedicalForms_healthhistory_delete',[['admin/MedicalForms/healthhistory/%(_0)s/delete/',['_0',]]],],['admin:MedicalForms_healthhistory_history',[['admin/MedicalForms/healthhistory/%(_0)s/history/',['_0',]]],],['admin:MedicalForms_musclejoint_add',[['admin/MedicalForms/musclejoint/add/',[]]],],['admin:MedicalForms_musclejoint_change',[['admin/MedicalForms/musclejoint/%(_0)s/',['_0',]]],],['admin:MedicalForms_musclejoint_changelist',[['admin/MedicalForms/musclejoint/',[]]],],['admin:MedicalForms_musclejoint_delete',[['admin/MedicalForms/musclejoint/%(_0)s/delete/',['_0',]]],],['admin:MedicalForms_musclejoint_history',[['admin/MedicalForms/musclejoint/%(_0)s/history/',['_0',]]],],['admin:account_emailaddress_add',[['admin/account/emailaddress/add/',[]]],],['admin:account_emailaddress_change',[['admin/account/emailaddress/%(_0)s/',['_0',]]],],['admin:account_emailaddress_changelist',[['admin/account/emailaddress/',[]]],],['admin:account_emailaddress_delete',[['admin/account/emailaddress/%(_0)s/delete/',['_0',]]],],['admin:account_emailaddress_history',[['admin/account/emailaddress/%(_0)s/history/',['_0',]]],],['admin:account_emailconfirmation_add',[['admin/account/emailconfirmation/add/',[]]],],['admin:account_emailconfirmation_change',[['admin/account/emailconfirmation/%(_0)s/',['_0',]]],],['admin:account_emailconfirmation_changelist',[['admin/account/emailconfirmation/',[]]],],['admin:account_emailconfirmation_delete',[['admin/account/emailconfirmation/%(_0)s/delete/',['_0',]]],],['admin:account_emailconfirmation_history',[['admin/account/emailconfirmation/%(_0)s/history/',['_0',]]],],['admin:app_list',[['admin/%(app_label)s/',['app_label',]]],],['admin:auth_group_add',[['admin/auth/group/add/',[]]],],['admin:auth_group_change',[['admin/auth/group/%(_0)s/',['_0',]]],],['admin:auth_group_changelist',[['admin/auth/group/',[]]],],['admin:auth_group_delete',[['admin/auth/group/%(_0)s/delete/',['_0',]]],],['admin:auth_group_history',[['admin/auth/group/%(_0)s/history/',['_0',]]],],['admin:auth_user_password_change',[['admin/users/user/%(_0)s/password/',['_0',]]],],['admin:index',[['admin/',[]]],],['admin:jsi18n',[['admin/jsi18n/',[]]],],['admin:login',[['admin/login/',[]]],],['admin:logout',[['admin/logout/',[]]],],['admin:password_change',[['admin/password_change/',[]]],],['admin:password_change_done',[['admin/password_change/done/',[]]],],['admin:sites_site_add',[['admin/sites/site/add/',[]]],],['admin:sites_site_change',[['admin/sites/site/%(_0)s/',['_0',]]],],['admin:sites_site_changelist',[['admin/sites/site/',[]]],],['admin:sites_site_delete',[['admin/sites/site/%(_0)s/delete/',['_0',]]],],['admin:sites_site_history',[['admin/sites/site/%(_0)s/history/',['_0',]]],],['admin:socialaccount_socialaccount_add',[['admin/socialaccount/socialaccount/add/',[]]],],['admin:socialaccount_socialaccount_change',[['admin/socialaccount/socialaccount/%(_0)s/',['_0',]]],],['admin:socialaccount_socialaccount_changelist',[['admin/socialaccount/socialaccount/',[]]],],['admin:socialaccount_socialaccount_delete',[['admin/socialaccount/socialaccount/%(_0)s/delete/',['_0',]]],],['admin:socialaccount_socialaccount_history',[['admin/socialaccount/socialaccount/%(_0)s/history/',['_0',]]],],['admin:socialaccount_socialapp_add',[['admin/socialaccount/socialapp/add/',[]]],],['admin:socialaccount_socialapp_change',[['admin/socialaccount/socialapp/%(_0)s/',['_0',]]],],['admin:socialaccount_socialapp_changelist',[['admin/socialaccount/socialapp/',[]]],],['admin:socialaccount_socialapp_delete',[['admin/socialaccount/socialapp/%(_0)s/delete/',['_0',]]],],['admin:socialaccount_socialapp_history',[['admin/socialaccount/socialapp/%(_0)s/history/',['_0',]]],],['admin:socialaccount_socialtoken_add',[['admin/socialaccount/socialtoken/add/',[]]],],['admin:socialaccount_socialtoken_change',[['admin/socialaccount/socialtoken/%(_0)s/',['_0',]]],],['admin:socialaccount_socialtoken_changelist',[['admin/socialaccount/socialtoken/',[]]],],['admin:socialaccount_socialtoken_delete',[['admin/socialaccount/socialtoken/%(_0)s/delete/',['_0',]]],],['admin:socialaccount_socialtoken_history',[['admin/socialaccount/socialtoken/%(_0)s/history/',['_0',]]],],['admin:users_user_add',[['admin/users/user/add/',[]]],],['admin:users_user_change',[['admin/users/user/%(_0)s/',['_0',]]],],['admin:users_user_changelist',[['admin/users/user/',[]]],],['admin:users_user_delete',[['admin/users/user/%(_0)s/delete/',['_0',]]],],['admin:users_user_history',[['admin/users/user/%(_0)s/history/',['_0',]]],],['admin:view_on_site',[['admin/r/%(content_type_id)s/%(object_id)s/',['content_type_id','object_id',]]],],['djdt:render_panel',[['__debug__/render_panel/',[]]],],['djdt:sql_explain',[['__debug__/sql_explain/',[]]],],['djdt:sql_profile',[['__debug__/sql_profile/',[]]],],['djdt:sql_select',[['__debug__/sql_select/',[]]],],['djdt:template_source',[['__debug__/template_source/',[]]],],['home',[['',[]]],],['medical_appointments:appointments',[['appointments/',[]]],],['medical_appointments:get_clinics',[['appointments/clinics/',[]]],],['medical_appointments:new_appointments',[['appointments/new/',[]]],],['medical_appointments:timetable_doctor',[['appointments/timetable/',[]]],],['medical_appointments:timetable_patient',[['appointments/new/timetable/%(clinic)s',['clinic',]]],],['medical_forms:MVA_intake',[['medicalforms/MVA\u002Dintake/',[]]],],['medical_forms:accident_history',[['medicalforms/accident\u002Dhistory/',[]]],],['medical_forms:assessment',[['medicalforms/assessment/',[]]],],['medical_forms:health_history',[['medicalforms/health\u002Dhistory/',[]]],],['medical_forms:patient_info',[['medicalforms/patient\u002Dinformation/',[]]],],['medical_forms:subjective_eval',[['medicalforms/subjective\u002Devaluation/',[]]],],['socialaccount_connections',[['accounts/social/connections/',[]]],],['socialaccount_login_cancelled',[['accounts/social/login/cancelled/',[]]],],['socialaccount_login_error',[['accounts/social/login/error/',[]]],],['socialaccount_signup',[['accounts/social/signup/',[]]],],['users:account_login',[['users/login/',[]]],],['users:account_logout',[['users/logout/',[]]],],['users:account_redirect',[['users/~redirect/',[]]],],['users:account_signup',[['users/signup/',[]]],],['users:account_signup_doctors',[['users/signup/doctors/',[]]],],['users:doctor_profile',[['users/doctor/%(username)s/',['username',]]],],['users:list',[['users/',[]]],],['users:patient_doctor_redirect',[['users/%(username)s/',['username',]]],],['users:patient_profile',[['users/patient/%(username)s/',['username',]]],],['users:user_settings',[['users/~settings/',[]]]]];self.url_patterns={};for(_i=0,_len=url_patterns.length;_i<_len;_i++){_ref=url_patterns[_i],name=_ref[0],pattern=_ref[1];self.url_patterns[name]=pattern;Urls[name]=_get_url(name);Urls[name.replace(/-/g,'_')]=_get_url(name);}
return Urls;})();